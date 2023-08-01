output = ""
with open('old_japanese.tsv',encoding="utf-8") as f:
    for line in f:
        if line[:4]=="def_":
            try: 
                data = line.split("	")
                def_name = data[0]
                disp_name = data[2]
                jp_name = data[3]
                jp_name = jp_name.replace("\n","")
                new_data = f"{def_name}		{disp_name}	{jp_name}({disp_name})"
                new_data += "\n"
                output += new_data
            except:
                pass
        else:
            output += line
with open('japanese.tsv', 'w', encoding='utf-8') as f:
    f.write(output)
