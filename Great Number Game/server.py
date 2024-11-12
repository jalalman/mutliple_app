from flask import Flask ,redirect,render_template,session,request,url_for
import random
app=Flask('__name__')
app.secret_key='random number'
@app.route('/',methods=['GET','POST'])
def landing():
    result_div=''
    user_num=0
    won=False

    if 'num' not in session:
        session['num']=random.randint(1,100)
        session['guess']=0



    ran_num=session['num']


    if request.method =='POST':
        session['input_num']=int(request.form.get('guessed',0))
        user_num=session['input_num']
        if user_num > ran_num :
            result_div="<div class='red show'>guess lower</div>"
            session['guess']+=1
        elif user_num < ran_num :
            result_div="<div class='blue show'>guess higher</div>"
            session['guess']+=1
        elif user_num == ran_num:
            won=True
            result_div="<div class='green show'>YOU WIN</div>"
            session.pop('num')
    return render_template('index.html',result=result_div,user=user_num,rand=ran_num,won=won,guess=session['guess'])

@app.route('/reset')
def reset():
    session.pop('num', None)
    session.pop('guess',1)
    return redirect(url_for('landing'))

if __name__== '__main__':
    app.run(debug=True)