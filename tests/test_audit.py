import csv, tempfile, unittest
from pathlib import Path
from audit import audit

class AuditTests(unittest.TestCase):
    def test_groups_service_costs(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'bill.csv'
            p.write_text('service,cost\nCompute,10\nCompute,5\nStorage,2\n', encoding='utf-8')
            r = audit(p)
            self.assertEqual(r['total_cost'], 17.0)
            self.assertEqual(r['services'][0]['service'], 'Compute')
            self.assertEqual(r['services'][0]['cost'], 15.0)

if __name__ == '__main__': unittest.main()
