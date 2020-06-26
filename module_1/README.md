# Movies IMDb 
## DataFrame research from csv file of movies database
Need to answer 27 quiz questions. As a result 27 answers were received.

## Remarks
- It seems functions that are in preprocessing module maybe too hard. In a moment I got this idea about separate dataframes for columns that have many elements in string. But I spent too much time for realizing this idea. It would be nice to know other variants of decision. In some questions I used df.stack() method, but in some questions I don't know how to solve without my written function.
- About two films that have the same names ("The Gift", "Fantastic Four"): I don't quite understand whether need to rename in dataframe such equal objects or not. It would be great to know your opinion about this matter.
- One string in movies dataframe (number 86 if open in Excel file) is cutted, just some data at the end is left. When doing read_csv created dataframe pasted indexes bypassing this string. Is it ok to deal with it or need to make up for data in this string first in csv file (f.e. by searching in internet for this movie), or maybe to delete it at all?
- Problem with encoding in file. Some names of actors or even names of movies have not readable symbols. I spent much time to solve problem with encoding russian movie "Сталинград". Online decoders in internet showed that it's cp1252, but doing encode->decode operations I got not needed symbols. Maybe it's several times encoding there. Need your support in solving such questions.