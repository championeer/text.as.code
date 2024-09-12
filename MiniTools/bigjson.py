"""
 作者：XYU with Cursor and Claude
 版本：1.0

 说明：
 这个脚本用于处理大json文件
"""

import ijson
import json

def process_large_json(input_file, output_file):
    # Open the input file in binary mode
    with open(input_file, 'rb') as file:
        # Create a parser
        parser = ijson.parse(file)
        
        # Open the output file
        with open(output_file, 'w') as out_file:
            # Start the JSON array
            out_file.write('[\n')
            
            is_first = True
            for prefix, event, value in parser:
                # Process each item in the root array
                if prefix == '' and event == 'start_map':
                    if not is_first:
                        out_file.write(',\n')
                    else:
                        is_first = False
                    
                    # Parse the entire object
                    object_content = ijson.ObjectBuilder()
                    ijson.ObjectBuilder.event(object_content, event, value)
                    for _, inner_event, inner_value in parser:
                        ijson.ObjectBuilder.event(object_content, inner_event, inner_value)
                        if inner_event == 'end_map':
                            break
                    
                    # Write the formatted JSON object
                    json.dump(object_content.value, out_file, indent=2)
            
            # End the JSON array
            out_file.write('\n]')

# Usage
input_file = '/Users/qianli/Sync/tana_ws@2024-08-30.json'
output_file = '/Users/qianli/Sync/tana_ws@2024-09-02.json'
process_large_json(input_file, output_file)