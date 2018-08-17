################## Downloading files from WEB ################

from urllib import request
# Download the contents and store it a variable goog_url
goog_url = "http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportUsersSample.csv"

# Create a function to 
def download_stock_data(csv_url):
	response = request.urlopen(csv_url) #Connect to the internet and keep alive
	csv = response.read()               # Read the data and store it on variable csv
	csv_str = str(csv)                  # Whatever data is read, convert it to string for unifermity
	lines = csv_str.split("\\n")        # Breaks a line and store it in variable lines
	dest = r'/Users/bikrdas/Desktop/google_stuck.csv'          # Store the file in local 
	fw = open(dest, 'w')                # Open the file to write the contents
	for line in lines:
		fw.write(line + "\n")           # For each line read , write it to the dest with new line for each line
	fw.close()

download_stock_data(goog_url)
