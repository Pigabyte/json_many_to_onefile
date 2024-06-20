import os
import glob
import json

#global Variables

dictionary = {
  "types": {
    "npc": {
      "loots": {
          }
        }
      }
    };

dict_output_file={};

def fresh_file():
    with open('FileGenerated.json','w') as Generatedfile2:
        clear = '';
        Generatedfile2.write(clear);
        

def open_copy():
    global dictionary;
    global dict_output_file;
    filename_list = glob.glob("*.log");
    for filename in filename_list:
        kill_counter = 1;
        drops_dict = {};
        dictionary1 = {};
        #print(filename_list);
        with open(filename,"r") as file_handler , open('FileGenerated.json','a+') as Generatedfile2:
            for line in file_handler:
                #print(filename);
                #print(line);
                line_json = json.loads(line);
                line_json_name = line_json["name"];
                #line_json_quantity = line_json["quantity"];
                line_drops = line_json["drops"];
                list_events = kill_counter;
                kill_counter += 1;
                for line_data_drops in line_drops:
                    #print(line_data_drops); 
                    if (str(line_data_drops['id']) not in drops_dict):
                        drops_dict.update({str(line_data_drops["id"]) : line_data_drops["quantity"]});
                    else:
                        drops_dict[str(line_data_drops["id"])] += line_data_drops["quantity"]; 
                    #print(drops_dict);
                        dictionary1.update({line_json["name"] : {"first" : 1656630436286, "last": 1656700791090, "events" : list_events, "drops" : drops_dict}});
            #dictionary["types"]["npc"]["loots"];              
            #print(line_json_name);
            #print(dictionary1);
        dictionary["types"]["npc"]["loots"].update(dictionary1);
    #print(dictionary);
    # ---------------------------- Dictionary to String 
    dict_string = str(dictionary);
    dict_replace1 = dict_string.replace("'",'"');
    # ---------------------------- Problem fixing ----------------------------
    dict_replace2 = dict_replace1.replace('Kree"arra',"Kree'arra");
    dict_replace2 = dict_replace2.replace('K"ril',"K'ril");
    dict_replace2 = dict_replace2.replace('Vet"ion',"Vet'ion");
    dict_replace2 = dict_replace2.replace('Zakl"n',"Zakl'n");
    dict_replace2 = dict_replace2.replace('Scorpia"s',"Scorpia's");
    # ---------------------------- Line breaking (just so I can read code in multiple lines)
    dict_replace3 = dict_replace2.replace("{" , "\t{\n");
    dict_replace3 = dict_replace3.replace("}," , "\t},\n");
    print(dict_replace3);
    # ---------------------------- Final Product
    with open(filename,"r") as file_handler , open('FileGenerated.json','a+') as Generatedfile2:
        dict_output_file = dict_replace3;   
        Generatedfile2.write(dict_output_file);
        print("\n -------------------------- FILE GENERATED (Check the Folder for 'FileGenerated.json') ------------------------");
fresh_file();   
open_copy();
