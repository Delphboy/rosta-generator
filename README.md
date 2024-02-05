# Rosta Generator

Create a rotating rosta schedule for $n$ employees over $w$ weeks. Rostas are stored as CSV file which can be converted to an `xlsx` file in Excel (using Save As... and changing the file type)

```bash
main.py --people 14 \
        --days_in 5 \
        --days_out 2 \
        --weeks 52 \
        --output "rosta.csv"
```