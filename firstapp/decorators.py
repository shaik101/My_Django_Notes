
def decorator1(demo):

    def wrap(request,*args,**kwargs):

        if args:
            print(args)
            return demo(request,*args,**kwargs)
        else:
            return ValueError
    
    return wrap

