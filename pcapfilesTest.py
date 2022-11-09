
# import required module
import os
# assign directory
directory = 'C:/Users/Aaron/PCAP_Files'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(str(f))