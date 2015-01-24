%rng('default');

ratio = 0.1;

fid1 = fopen('../data/train.csv','r'); %# open csv file for reading
fid2 = fopen('../data/random1on100.csv','w'); %# open new csv file
fid3 = fopen('../data/random1on100indexes.csv','w'); %# open new csv file
i = 1;
rands = rand(1e8,1);

line = fgets(fid1); %# read first line
fprintf(fid2,'%s',line); %# write the line to the new file
fprintf(fid3,'%d \n',i);

while ~feof(fid1)
    if rands(i) < ratio
        line = fgets(fid1); %# read line by line
        fprintf(fid2,'%s',line); %# write the line to the new file
        fprintf(fid3,'%d \n',i); %write the index
    end
    i = i+1;
end
fclose(fid1);
fclose(fid2);
fclose(fid3);