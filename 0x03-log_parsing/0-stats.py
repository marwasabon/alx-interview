#!/usr/bin/python3

"""Write a script that reads stdin line by line and computes metrics"""

import sys
 

def display_metrics(status_counts, total_size):  
    """Displays the aggregated statistics."""  
    print("File size: {}".format(total_size))  
    for code in sorted(status_counts.keys()):  
        if status_counts[code] > 0:  
            print("{}: {}".format(code, status_counts[code]))  

def main():  
    line_count = 0  
    total_size = 0  

    status_codes = {  
        "200": 0,   
        "301": 0,   
        "400": 0,   
        "401": 0,   
        "403": 0,  
        "404": 0,   
        "405": 0,   
        "500": 0  
    }  

    try:  
        for entry in sys.stdin:  
            if line_count > 0 and line_count % 10 == 0:  
                display_metrics(status_codes, total_size)  

            parts = entry.split()  
            line_count += 1  

            try:  
                total_size += int(parts[-1])  
            except (IndexError, ValueError):  
                pass 

            if len(parts) >= 2:  
                status_code = parts[-2]  
                if status_code in status_codes:  
                    status_codes[status_code] += 1  

        display_metrics(status_codes, total_size)  

    except KeyboardInterrupt:  
        display_metrics(status_codes, total_size)  
        raise  

if __name__ == "__main__":  
    main()