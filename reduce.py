def myreduce(function,sequence,initial=None):
    if initial !=None:
        if not sequence:
            return initial
        else:
            first = function(sequence[0],initial)
            for x in sequence[1:]:
                first = function(first,x)
            return first
    else:
        first =sequence[0]
        for x in sequence[1:]:
                first = function(first,x)
        return first


