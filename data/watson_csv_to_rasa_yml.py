import sys
import pandas as pd
from tqdm import tqdm 

def convert_csv_to_yml(read_filename, write_filename):
    df = pd.read_csv(read_filename, header = None, names = ['Question', 'Intent'])
    file_object = open(write_filename, 'w')
    labels = set(df.Intent)
    for label in tqdm(labels):
        #print('## intent:' + label)
        file_object.write('## intent:' + label + '\n')
        questions = list( df[df.Intent == label]['Question'] )
        for question in questions:
            #print('- ' + question)
            file_object.write('- ' + question + '\n')
    file_object.close()

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '-help'] :
        print('''
        Please provide 2 inputs to the scripts in the foillowing order:
        1. Data file exported from IBM Watson Assistant (csv file format)
        2. Target filename to be used as RASA training data (yml format)
        
        Usage example:
        $ python3 watson_csv_to_rasa_yml.py watson_intents.csv nlu.md
        ''')
        
    elif len(sys.argv) == 3:
        watson_filename = sys.argv[1]
        rasa_filename = sys.argv[2]
        convert_csv_to_yml(watson_filename, rasa_filename)
        print('RASA intent data file created successfully.')
        
    else:
        print('!!! Please refer to help. Use -h or -help.')
        
    
    
    

