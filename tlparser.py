from flask import Flask, render_template
import jsonify
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    
    #return _test_
#    _filenamo_ = sys.argv[-1]
    _textfile_ = open("Time.txt", "r")

    _dic_ = dict()
    i=0
    _tim_=''

    _test_=[]
    for _lin_ in _textfile_:

        _lin_ = _lin_.strip(":")
        _lin_ = _lin_.upper()
        #_lin_ = _lin_.replace("")
        _wrds_ = _lin_.split(" ")

        #print(_wrds_)


        for _swrd_ in _wrds_:

            if "PM" in _swrd_[-2:] or "AM" in _swrd_[-2:]:


            #    print(_swrd_)
                if i>0:

                    try:
                        time_1 = datetime.strptime(_tim_,"%I:%M%p")
                        time_2 = datetime.strptime(_swrd_,"%I:%M%p")
                        time_i = time_2 - time_1
                        #print(time_i.seconds/3600)
                        _test_.append(time_i.seconds/3600)

                        _tim_=''
                        i=0
                    except Exception as e:
                        exception_type, exception_object, exception_traceback = sys.exc_info()
                        print("--------------------------------------")

                        line_number = exception_traceback.tb_lineno
                        print("There is Time Format error in Time LOG LINE:", line_number)
                        print("---------------------------------------")
                else:
                    i=i+1
                    #print(i)

                _tim_ = _swrd_

            else:
                _dic_[_swrd_]=1
    print("------------------Individual Hours---------------------------")
    print("Individual Hours:",_test_)
    print("--------------------Total Spent Hours------------------------")
    #return "{sum(_test_)}"
    #return jsonify(_test_)
    print("Total Spent Hours ==>",sum(_test_))
    sumtime = sum(_test_)
    return render_template('hello.html', _test_=_test_, sumtime=sumtime, line_number=line_number)





if __name__ == '__main__':
    import sys
    from datetime import datetime
    app.run(debug=True) 
