log_lines = [
	    "Failed password for admin from 203.0.113.5",
    "Accepted password for lucy from 192.0.2.10",
    "Failed password for root from 203.0.113.5",
    "Failed password for root from 198.51.100.7",
    "Failed password for admin from 203.0.113.5",
    "Accepted password for lucy from 192.0.2.10",
]

for lines in log_lines:
	if "Failed" in lines:
		words = lines.split()
		print (words[-1])
