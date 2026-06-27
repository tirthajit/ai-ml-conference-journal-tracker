const DATA_BASE = 'https://raw.githubusercontent.com/tirthajit/ai-ml-conference-journal-tracker/main/data/';

const TABLES = {
  calendar: {
    file: 'submission_calendar_current_cycle.csv',
    columns: ['curated_tier','acronym','current_or_next_edition','area','full_paper_deadline','timezone','deadline_status','deadline_confidence','official_or_tracker_url','last_verified'],
    labels: {curated_tier:'Tier', acronym:'Venue', current_or_next_edition:'Edition', area:'Area', full_paper_deadline:'Deadline', timezone:'TZ', deadline_status:'Status', deadline_confidence:'Confidence', official_or_tracker_url:'Source', last_verified:'Verified'},
    filters: ['curated_tier','area','deadline_confidence','deadline_status'],
    sortKey: 'full_paper_deadline'
  },
  conferences: {
    file: 'conferences_master.csv',
    columns: ['curated_tier','acronym','name','area','core_rank_prefill','current_or_next_edition','full_paper_deadline','deadline_confidence','usual_tentative_window','relevance_tags','official_or_tracker_url'],
    labels: {curated_tier:'Tier', acronym:'Acronym', name:'Name', area:'Area', core_rank_prefill:'CORE', current_or_next_edition:'Edition', full_paper_deadline:'Deadline', deadline_confidence:'Confidence', usual_tentative_window:'Usual window', relevance_tags:'Tags', official_or_tracker_url:'Source'},
    filters: ['curated_tier','area','deadline_confidence'],
    sortKey: 'rank_order'
  },
  journals: {
    file: 'journals_reputable.csv',
    columns: ['target_priority','journal','area','publisher','jcr_quartile_or_rank_note','sjr_quartile_note','metric_source_url','journal_url','relevance_tags','last_verified'],
    labels: {target_priority:'Priority', journal:'Journal', area:'Area', publisher:'Publisher', jcr_quartile_or_rank_note:'JCR note', sjr_quartile_note:'SJR note', metric_source_url:'Metrics', journal_url:'Journal page', relevance_tags:'Tags', last_verified:'Verified'},
    filters: ['target_priority','area','publisher'],
    sortKey: 'target_priority'
  },
  sources: {
    file: 'sources.csv',
    columns: ['source_name','role','url'],
    labels: {source_name:'Source', role:'Role', url:'URL'},
    filters: ['role'],
    sortKey: 'source_name'
  }
};

function parseCSV(text) {
  const rows = [];
  let row = [], field = '', inQuotes = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i], n = text[i+1];
    if (c === '"' && inQuotes && n === '"') { field += '"'; i++; continue; }
    if (c === '"') { inQuotes = !inQuotes; continue; }
    if (c === ',' && !inQuotes) { row.push(field); field = ''; continue; }
    if ((c === '\n' || c === '\r') && !inQuotes) {
      if (c === '\r' && n === '\n') i++;
      row.push(field); field = '';
      if (row.some(v => v !== '')) rows.push(row);
      row = [];
      continue;
    }
    field += c;
  }
  if (field || row.length) { row.push(field); rows.push(row); }
  const headers = rows.shift() || [];
  return rows.map(r => Object.fromEntries(headers.map((h, i) => [h, r[i] || ''])));
}

function esc(s) {
  return String(s ?? '').replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
}

function badge(value, type) {
  const v = esc(value || '');
  const cls = ['badge'];
  const low = String(value || '').toLowerCase();
  if (type === 'tier') cls.push('tier-' + low);
  if (low.includes('official')) cls.push('official');
  if (low.includes('tentative') || low.includes('tracker')) cls.push('tentative');
  if (low === 'passed') cls.push('passed');
  if (low === 'upcoming') cls.push('upcoming');
  return `<span class="${cls.join(' ')}">${v}</span>`;
}

function formatCell(key, val) {
  if (!val) return '';
  if (key === 'curated_tier' || key === 'target_priority') return badge(val, 'tier');
  if (key === 'deadline_confidence' || key === 'deadline_status') return badge(val);
  if (key.includes('url')) return `<a href="${esc(val)}" rel="noopener">Source</a>`;
  if (key === 'journal_url') return `<a href="${esc(val)}" rel="noopener">Journal</a>`;
  return esc(val);
}

function uniqueValues(rows, key) {
  return [...new Set(rows.map(r => r[key]).filter(Boolean))].sort((a,b) => a.localeCompare(b));
}

function sortRows(rows, key) {
  return [...rows].sort((a,b) => {
    const av = a[key] || '', bv = b[key] || '';
    const an = Number(av), bn = Number(bv);
    if (!Number.isNaN(an) && !Number.isNaN(bn)) return an - bn;
    return av.localeCompare(bv);
  });
}

function makeToolbar(tableId, spec, rows) {
  const filters = spec.filters.map(key => {
    const opts = uniqueValues(rows, key).map(v => `<option value="${esc(v)}">${esc(v)}</option>`).join('');
    return `<select data-filter="${key}" aria-label="Filter by ${esc(spec.labels[key] || key)}"><option value="">All ${esc(spec.labels[key] || key)}</option>${opts}</select>`;
  }).join('');
  return `<div class="table-toolbar"><input type="search" placeholder="Search table" aria-label="Search table" data-search>${filters}</div>`;
}

function renderTable(container, tableId, rows, spec, limit) {
  const cols = spec.columns;
  const head = cols.map(c => `<th>${esc(spec.labels[c] || c)}</th>`).join('');
  const bodyRows = rows.slice(0, limit || rows.length).map(r => `<tr>${cols.map(c => `<td>${formatCell(c, r[c])}</td>`).join('')}</tr>`).join('');
  const body = bodyRows || `<tr><td colspan="${cols.length}" class="empty">No matching rows.</td></tr>`;
  container.querySelector('[data-count]').textContent = `${Math.min(rows.length, limit || rows.length)} of ${rows.length} rows shown`;
  container.querySelector('[data-table-wrap]').innerHTML = `<table><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table>`;
}

async function initTable(container) {
  const tableId = container.dataset.table;
  const spec = TABLES[tableId];
  if (!spec) return;
  container.innerHTML = '<p class="loading">Loading data…</p>';
  try {
    const res = await fetch(DATA_BASE + spec.file, {cache: 'no-store'});
    if (!res.ok) throw new Error('Could not load CSV');
    let rows = parseCSV(await res.text());
    rows = sortRows(rows, spec.sortKey);
    if (container.dataset.upcoming === 'true') {
      rows = rows.filter(r => (r.deadline_status || '').toLowerCase() === 'upcoming');
    }
    const defaultLimit = Number(container.dataset.limit || 0) || null;
    container.innerHTML = `${makeToolbar(tableId, spec, rows)}<div class="table-meta"><span data-count></span><a href="${DATA_BASE + spec.file}">Download CSV</a></div><div class="table-wrap" data-table-wrap></div>`;
    const search = container.querySelector('[data-search]');
    const filters = [...container.querySelectorAll('[data-filter]')];
    const apply = () => {
      const q = (search.value || '').toLowerCase().trim();
      let out = rows.filter(r => !q || Object.values(r).some(v => String(v).toLowerCase().includes(q)));
      for (const f of filters) {
        if (f.value) out = out.filter(r => r[f.dataset.filter] === f.value);
      }
      renderTable(container, tableId, out, spec, defaultLimit);
    };
    search.addEventListener('input', apply);
    filters.forEach(f => f.addEventListener('change', apply));
    apply();
  } catch (err) {
    container.innerHTML = `<p class="empty">Could not load table data. Open the CSV directly from the repository.</p>`;
  }
}

document.querySelectorAll('[data-table]').forEach(initTable);

const toggle = document.querySelector('[data-nav-toggle]');
const nav = document.querySelector('[data-nav]');
if (toggle && nav) {
  toggle.addEventListener('click', () => nav.classList.toggle('open'));
}
