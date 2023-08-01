#!/usr/bin/env ruby
#A regular expression that outputs [SENDER], [RECEIVER], [FLAGS]
puts ARGV[0].scan(/\[from:(.*?)\]\s\[flags:(.*?)\]/).join(',')
