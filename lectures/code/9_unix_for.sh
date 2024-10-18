# Descending into a directory structure
# and running some commands in each directory
cwd=`pwd`
for dir in `find. -type d`
do
    cd $dir
    <execute commands>
    cd $cwd
done