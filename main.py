#If it is not built-in module u can install it
import re

# Email regex pattern. You can customize it
email_regex = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'


# Store results
line_email_counts = {}
all_emails = []

# Output log content
log_output = ""

with open("emails.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        emails_found = re.findall(email_regex, line)
        if emails_found:
            line_email_counts[line_number] = emails_found
            all_emails.extend(emails_found)
            log_output += f"Line {line_number}: {len(emails_found)} email(s) -> {emails_found}\n"

# Find lines with most emails
if line_email_counts:
    max_count = max(len(v) for v in line_email_counts.values())
    max_lines = [line for line, emails in line_email_counts.items() if len(emails) == max_count]
    
    log_output += "\n🔝 Line(s) with most emails:\n"
    for line in max_lines:
        log_output += f"  ➤ Line {line} with {len(line_email_counts[line])} email(s): {line_email_counts[line]}\n"
else:
    log_output += "❌ No emails found in the file.\n"

log_output += f"\n📦 Total emails found: {len(all_emails)}\n"

# Print to console
print(log_output)

# Save to logs.txt
with open("logs.txt", "w") as log_file:
    log_file.write(log_output)
