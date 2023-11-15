def automted_file_creator(directory_name):
    """
    goes in the directory provided, reads the files' names and
    create new sub directories based on the names of the files,
    reads data from each file, and make directories based on the data
    inside the files in each respective directory

    Args:
        directory_name (dir_path): where the files are located 
    """

    import os
    print('Started...')

    files = []
    for dir_name, dirnames, filenames in os.walk(directory_name):
        files.append(filenames)
    files = files[0][1:]
 
    for i in files:
        print("file : ", i) # remove
        counter = 1
        os.mkdir(directory_name + i.replace('.txt','/'))    
        print("Made directory named : ", (directory_name + i.replace('.txt','/')) ) # remove
        with open(directory_name+i, 'r') as f:
            for line in f:
                os.mkdir((directory_name+i.replace('.txt','/')+f"{counter}-"+line.replace('\n','').replace(' ','-').replace('|','')) ) 
                print('Made sub directory named : ', (directory_name+i.replace('.txt','/')+f"{counter}-"+line.replace('\n','').replace(' ','-').replace('|','')) ) # remove
                counter += 1
            
automted_file_creator("e:/100-ML-Projects/")


