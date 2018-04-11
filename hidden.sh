hdfs dfs -put /home/hadoop/Downloads/* input_lab2
hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.4.jar -mapper mapper.py -reducer reducer.py -input  input_lab2 -output input_lab2_output 

hdfs dfs -cat input_lab2_output/* > out.txt

python find_top_words.py

hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.4.jar -mapper mapper2.py -reducer reducer.py -input input_lab2 -output input_lab2_ext_output 

hdfs dfs -cat input_lab2_ext_output/* > out_ext.txt

python convertinput.py
python convertinputext.py




