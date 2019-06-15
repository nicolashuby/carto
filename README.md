array=[["CAMP11WDP", {"host"=>"cambrai","port"=>"50001"}],
["CAMP12WDP", {"host"=>"cambrai","port"=>"50002"}],
["VILP11WDP", {"host"=>"villeneuve","port"=>"50001"}],
["VILP12WDP", {"host"=>"villeneuve","port"=>"50002"}],
["CHAP11WDP", {"host"=>"chat","port"=>"50001"}],
["CHAP12WDP", {"host"=>"chat","port"=>"50002"}]]

array_host=[]
array.each { |instances,values|
    unless array_host.include?(values["host"]) 
    	array_host << values["host"]
    	puts instances
    	puts values
    end
}
