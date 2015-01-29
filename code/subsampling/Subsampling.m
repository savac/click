%rng('Default');

ratio = 0.01;

fid1 = fopen('../../data/train.csv','r'); %# open csv file for reading
fid2 = fopen('../../data/validationAllDays.csv','w'); %# open new csv file
%fid3 = fopen('../data/random1on100indexes.csv','w'); %# open new csv file

line = fgets(fid1); %# read first line
fprintf(fid2,'%s',line); %# write the line to the new file
%fprintf(fid3,'%d \n',i);

while ~feof(fid1)
    line = fgets(fid1); %# read line by line
    if rand(1) < ratio
        fprintf(fid2,'%s',line); %# write the line to the new file
        %fprintf(fid3,'%d \n',i); %write the index
    end
end
fclose(fid1);
fclose(fid2);
%fclose(fid3);