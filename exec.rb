dirs = Dir[File.join(ARGV[0], '*')]
dirs.each do |d|
	system "duplicateimagefinder/app.py -d '#{d}' -c 97"
end
