# Gaode-API-automatic-query
Use selenium to automatically search the latitude and longitude coordinates of the address on Gaode API and insert the specified location in the specified CSV file
The specific steps are to control the browser through selenium, and input the address into the search box. Because Gaode API can't crawl the obtained results, click the copy button through selenium, and then copy the results to the website created by Django to get the results and input them into the CSV file.
