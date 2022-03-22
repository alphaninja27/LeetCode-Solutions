class MyQueue {
public:
    stack<int>s1;
stack<int>s2;
MyQueue() {
    
}

void push(int x) {
    s1.push(x);
}

int pop() {
    int x;
    if(s2.size()>=1)
    {
        x=s2.top();
        s2.pop();
        return x;
    }
    else
    {
        while(s1.size()>=1)
        {
            x=s1.top();
            s2.push(x);
            s1.pop();
        }
        x=s2.top();
        s2.pop();
        return x;
    }
}

int peek() {
    int x;
    if(s2.size()>=1)
    {
        return s2.top();
    }
    else
    {
        while(s1.size()>=1)
        {
            x=s1.top();
            s2.push(x);
            s1.pop();
        }
        return s2.top();
    }
}

bool empty() {
    if(s1.size()>=1 || s2.size()>=1)
        return false;
    return true;
    }
};
