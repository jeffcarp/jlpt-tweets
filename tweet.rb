require 'json'
require 'twitter'
require 'time'

# open vocab array
input = JSON.parse(IO.read('/home/jeff/gh/jeffcarp/jlpt-tweets/vocab-shuffle.json'))

# pick a vocab item
# the offset is hard coded to be the number of days past 12/1/2013
offset = (Date.today - Date.new(2013, 12, 1)).to_i

word = input[offset]

raise "No word" if !word

puts Time.now.utc.iso8601
puts word.inspect

client = Twitter::REST::Client.new do |config|
  config.consumer_key        = ENV['JLPT_TWTR_CONSUMER_KEY']
  config.consumer_secret     = ENV['JLPT_TWTR_CONSUMER_SECRET']
  config.access_token        = ENV['JLPT_TWTR_ACCESS_TOKEN']
  config.access_token_secret = ENV['JLPT_TWTR_ACCESS_TOKEN_SECRET']
end

# fix: put a space after commas in definition
word['english'] = word['english'].gsub ',', ', '

word['english'].strip!

str = ""
if word['kanji'] && word['kanji'] != word['hiragana']
  str += "#{word['kanji']} - #{word['hiragana']}\n#{word['english']}"
else
  str += "#{word['hiragana']}\n#{word['english']}"
end

puts str

if str.length
  client.update(str)
end
