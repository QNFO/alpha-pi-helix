INSERT OR REPLACE INTO resources (id, type, name, protection, status, metadata, created_at, updated_at, external_ids)
VALUES (
  'r2:alpha-pi-helix',
  'r2_bucket',
  'alpha-pi-helix',
  'standard',
  'active',
  '{"project":"QNFO.RSCH.APH","purpose":"Project archive for alpha-pi-helix research","storage_class":"Standard"}',
  datetime('now'),
  datetime('now'),
  '{}'
);

INSERT OR REPLACE INTO resources (id, type, name, protection, status, metadata, created_at, updated_at, external_ids)
VALUES (
  'github:QNFO/alpha-pi-helix',
  'github_repo',
  'alpha-pi-helix',
  'public',
  'active',
  '{"project":"QNFO.RSCH.APH","purpose":"Primary source repository","url":"https://github.com/QNFO/alpha-pi-helix"}',
  datetime('now'),
  datetime('now'),
  '{"github":"QNFO/alpha-pi-helix"}'
);
