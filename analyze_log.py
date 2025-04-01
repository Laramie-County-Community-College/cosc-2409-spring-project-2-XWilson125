import re
import os
import genLogFile #allows me to use a function near the end of analyze_log.py: generate_log_file()

def analyze_log_file(filename="access.log"):
    """Analyzes a log file and extracts information.

    **Instructions:**
    1. Complete the `extract_log_data` function to extract timestamp, IP address, URL, and status code from each valid log line.
    2. (Optional) Implement the `count_status_codes` function to count occurrences of each status code.

    This function opens the log file, reads each line, and performs analysis based on the extracted data.
    """
    error_count = 0 # set up variables to store the datetime, error count, unique IPs, and URL counts for the log file.
    unique_ip = set()
    url_counts = {}
    try:
        with open(filename, 'r') as log_file:   #open log file
            log_lines = log_file.readlines()    #read the lines into a list
            for line in log_lines:
                timestamp, ip, url, status_code = extract_log_data(line) #extract information
                datetime = timestamp            #stores datetime
                unique_ip.add(ip)               #update unique_ip set(automatically deletes input if not unique)
                try:                            #adds to an existing count of urls or adds a new url count
                    url_counts[url] = url_counts.get(url) + 1
                except:
                    url_counts[url] = 1
                if int(status_code) >= 400:
                    error_count += 1            #increments error count by one if there is an error.
        print('Total Errors (4xx and 5xx):', error_count)
        print('Unique IP Addresses:', len(unique_ip))
        print('URL access counts:')
        for section in url_counts:
            print('   ', end=' ')
            print(section, end=': ')
            print(url_counts[section])
    # d.  Print out the summary information as shown in the instructions.  It should look like this:
    except FileNotFoundError:
        print(f"Error: Log file '{filename}' not found.")
        return


def extract_log_data(line):
    #please note that you do not need to edit this function, just the analyze_log_file function above!
    #example usage: timestamp, ip, url, status_code = extract_log_data(line)
    
    
    """Extracts timestamp, IP address, URL, and status code from a valid log line.

    **Instructions:**
    1. Use regular expressions (re module) to extract the data from the log line format:
       - Timestamp (YYYY-MM-DD HH:MM:SS)
       - IP address (e.g., 192.168.1.1)
       - URL (everything after "GET ")
       - Status code (e.g., 200, 404)
    2. Return a tuple containing the extracted data (timestamp, ip, url, status_code)
    3. If the line format is invalid, return None for all data points.

   """

    match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \"GET (.+) HTTP/1.1\" (\d+)', line)
    if match:
        timestamp, ip, url, status_code = match.groups()
        return timestamp, ip, url, status_code
    else:
        return None, None, None, None



# Generate a sample log file (uncomment to create the file)
genLogFile.generate_log_file()

# Analyze the log file
analyze_log_file()