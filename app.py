#Code By-Shivansh Vasu


from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index2.html')


@app.route('/about')
def about():
     return render_template('about.html')

    
@app.route('/home')
def home2():
   return render_template('index2.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')



# @app.route('/sourcecode')
# def sourcecode():
#     return render_template('sourcecode.html')

# @app.route('/creator')
# def creator():
#     return render_template('creator.html')

 

@app.route('/' , methods=['POST','GET'])
def prediction():
    data1 = int(float(request.form['latitude']))
    data2 = int(float(request.form['longitude']))
    data3 = int(float(request.form['depth']))
    print(data1,data2,data3)
    arr = np.array([[data1, data2, data3]])
    output= model.predict(arr)


    def to_str(var):
     return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]
     
   
    # return render_template('prediction.html')
    print(output)
    if (output<=3):
        return render_template('predict1.html',p=to_str(output), q=' No ')
    elif (output>3 and output<=4):
        return render_template('predict2.html',p=to_str(output), q= ' Low ')
    elif (output>4 and output<7):
        return render_template('predict3.html',p=to_str(output), q=' Moderate ')
    elif (output>=7 and output<9):
        return render_template('predict4.html',p=to_str(output), q=' High ')
    elif (output>9):
        return render_template('predict5.html',p=to_str(output), q=' Very High ')
    else :
        return render_template('error.html')
    

if __name__ == "__main__":
    app.run(debug=True)






#Code By-Shivansh Vasu







