function get(selector, root = document) {
    return root.querySelector(selector);
}
const msgerForm = get(".msger-inputarea");
// const msgerInput = get(".msger-input");
// const msgerInput1 = get(".msger-input1");
const msgerInput2 = get(".msger-input2");
const msgerChat = get(".msger-chat");
const t = get(".table")
const submit_btn = document.getElementById("submit-btn");
const viewall_btn = document.getElementById("viewall-btn");
const passwd_box = document.getElementById("key-box");

// const ROOT_URL = `http://localhost:5000`

const ROOT_URL = "http://" + window.location.host

const TIME_UPDATECHAT = 3000 //1sec
const TIME_MINEBLOCK = 3000 // 1.1sec
const TIME_UPDATECHAIN = 6000 // 1.2sec

var messages = []
var USERNAME = null
var available_for_buy = []
var message_begin_sent = false //helps in updating chatbox when other guys send message but keep loading if we sent a msg from this side
// -----------------------------------------------

// Function to submit message
function submit_msg() {
    message_begin_sent = true
    // let loader = document.getElementById("rLoader");
    // loader.style.display = "block";
    // const receiver = msgerInput.value;
    // const type1 = msgerInput1.value
    const id = msgerInput2.value
    const passwd = passwd_box.value;
    // console.log(receiver)
    // console.log(type)
    // console.log(amount)
    if (id <1 || id> available_for_buy.length)
    {
        alert("Enter appropriate value");
        return;
    } 
        
    // document.getElementById("send_msg_field").value = ""; 
    // document.getElementById("send_msg_field1").value = "";
    document.getElementById("send_msg_field2").value = 0;
    console.log("sending add_msg request")
    var t = available_for_buy[id-1];
    api_url = ROOT_URL + "/add_transaction";
    let settings = {
        "url": api_url,
        "method": "POST",
        "headers": {
          "Content-Type": "application/json"
        },
        // "data": JSON.stringify({"msg": msgText, "username": USERNAME, "password": passwd})
        "data": JSON.stringify({"username": USERNAME, "receiver": t["receiver_alias"],"type":t["type"], "amount": t["amount"], "password": passwd})
    
    };

    $.ajax(settings).done(function (response) {
        // updateChatBox();
        // console.log("vover")
        mineBlock();
        console.log("mining finished")
        updateChain();
        console.log("update finished")
        removeAssetFromJSON(id)
        
        message_begin_sent = false
    });
}
function removeAssetFromJSON(id)
{
    api_url = ROOT_URL + "/remove_asset";
    let settings = {
    "url": api_url,
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    // "data": JSON.stringify({"msg": msgText, "username": USERNAME, "password": passwd})
    "data": JSON.stringify(available_for_buy[id-1])
    
    };
    $.ajax(settings).done(function (response) {
        console.log(response)
        allDeal(USERNAME);
    });
}
function viewall() {

    console.log("sending viewall request")
    api_url = ROOT_URL + "/view_user?name="+USERNAME;
    let settings = {
        "url": api_url,
        "method": "GET",
        // "data": JSON.stringify({"name": USERNAME})
        // "data": JSON.stringify({"username": USERNAME, "receiver": receiver, "amount": amount, "password": passwd})
    
    };

    $.ajax(settings).done(function (response) {
        // updateChatBox();
        console.log("vover")
        const transactions = response['transactions']
        console.log(transactions)
        var table = '<thead>  <tr> <th>Sender</th> <th> Receiver </th> <th> Type </th> <th> Amount </th> </tr> </thead> <tbody>';
        var rows = transactions.length;
        for( let i = 0;i < transactions.length ; i++ )
        {
            table+='<tr>'
            var s =  '<td>'+transactions[i]['sender_alias']+'</td>'
            table+=s
            var t = '<td>'+transactions[i]['receiver_alias']+'</td>'
            table+=t
            t = '<td>'+transactions[i]['type']+'</td>'
            table+=t;
            var f = '<td>'+transactions[i]['amount']+'</td>'
            table+=f;
            table+='</tr>'
            // appendMessage(transactions[i]['sender'],
            //     transactions[i]['receiver'],
            //     transactions[i]['amount'],
            //     "left" )
        }
        document.getElementById('table').innerHTML ='<table>' + table +'</tbody>' + '</table>';
        // message_begin_sent = false
    });
}

// -----------------------------------
// Helper Functions To Update Chatroom messages

function appendMessage(name, text, time, side) {
const msgHTML = `
    <div class="msg ${side}-msg">
    <div class="msg-bubble">
        <div class="msg-info">
            <div >Sender  :::  ${name}</div>
            <br>
            <div >Receiver :::  ${text}</div>
            <br>
            <div >Amount :::  ${time}</div>
            <br>
        </div>
    </div>
    </div>
    `;
    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
       // <div class="msg-text">${text}</div>
}

// function addResponseToMessages(response) {
//     mined_data = response['chain'];
//     unmined_data = response['unmined_msgs'];
//     if(messages.length == (mined_data.length+unmined_data.length-1)) {
//         console.log("Same length")
//         return;
//     }
//     messages = []
//     for(let i = 1; i < mined_data.length; ++i) {
//         data = mined_data[i]['data'];
//         for(let j = 0; j < data.length; ++j) {
//             messages.push(data[j]);
//         }
//     }
//     for(let i = 0; i < unmined_data.length; ++i) {
//         messages.push(unmined_data[i]);
//     }
// }

function updateChatBox() {
    console.log("user is ", USERNAME)
    console.log("Adding message")
    api_url = ROOT_URL + "/get_chain"
    let settings = {
        "url": api_url,
        "method": "GET"
    };
    $.ajax(settings).done(function (response) {
        let prev_msgs_len = messages.length;
        addResponseToMessages(response);
        if(prev_msgs_len === messages.length) {
            console.log("Upto-date");
            return;
        }
        console.log(messages)
        for(let i = prev_msgs_len; i < messages.length; ++i) {
            name = messages[i]['sender']
            text = messages[i]['msg']
            time = messages[i]['time']
            if(name == USERNAME)
                side = "right"
            else
                side = "left"
            appendMessage(name, text, time, side)
        }
        if(message_begin_sent != true) {
            let loader = document.getElementById("rLoader");
            loader.style.display = "none";
        }
    });
}
function allDeal (user){
            available_for_buy = []
            var api_url = ROOT_URL+ "/all_sales";
            console.log(api_url)
            let settings = {
            "url": api_url,
            "method": "GET",
            };      
            table = '';
        $.ajax(settings).done(function (response1) {
            // var chain = response['chain']
            // console.log(response1)
            var keys = ["ID", "Buyer", "Type", "Amount"];
            table = '<thead> <tr>';
            for ( let i = 0; i< keys.length;i++ )
                table+='<th>'+ keys[i] +'</th>';
            table+='</tr> </thead> <tbody>';
            var obkeys = Object.keys(response1["keys"])
            // console.log(obkeys)
            var k = 1;
            for( let j = 0 ;j < obkeys.length; j++ )
            {
                if(obkeys[j]=== user )
                    continue;
                var list = response1["keys"][obkeys[j]];
                for (i = 0 ; i < list.length ; i++)
                {
                    var r = list[i];
                    table+='<tr>'
                    var s =  '<td>'+k+'</td>'
                    table+=s
                    s =  '<td>'+r['receiver_alias']+'</td>'
                    table+=s
                    s =  '<td>'+r['type']+'</td>'
                    table+=s
                    s =  '<td>'+r['amount']+'</td>'
                    table+=s
                    table+='</tr>'
                    k++;
                    var obj = {}
                    obj["receiver_alias"] = r['receiver_alias'];
                    obj["receiver_id"] = r['receiver_id'];
                    obj["type"] = r['type'];
                    obj["amount"] = r["amount"];
                    available_for_buy.push(obj);
                }
            }
            document.getElementById('Table1').innerHTML ='<table>' + table +'</tbody> </table>';
            });
        }
$(document).ready(function() {
    // let loader = document.getElementById("lLoader");
    // loader.style.display = "block";
    USERNAME = document.getElementById("logout").value
    // updateChatBox();
    console.log("updated chat")
    
    allDeal(USERNAME);
    // loader.style.display = "none";
    // setInterval(function() {updateChatBox();}, TIME_UPDATECHAT);
    setInterval(function() {mineBlock();}, TIME_MINEBLOCK);
    setInterval(function() {updateChain();}, TIME_UPDATECHAIN);
});


// -------------------------------------------------------

// Helper functions to mine blocks

function mineBlock() {
    console.log("mining a block")
    let api_url = ROOT_URL + "/mine_block"
    let settings = {
        "url": api_url,
        "method": "GET"
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}



// Helper functions to update blockchain

function updateChain() {
    let api_url = ROOT_URL + "/replace_chain"
    let settings = {
        "url": api_url,
        "method": "GET"
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}


// Helper function to logout an user

function logout1() {
    console.log("Calling /logout in the server to decrease # of logged_in users")
    let api_url = ROOT_URL + "/logout"
    let settings = {
        "url": api_url,
        "method": "GET"
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function logout2() {
    console.log("Redirecting")
    window.location.href = ROOT_URL;
}
function logout() {
    mineBlock()
    logout1()
    setTimeout(function(){
        logout2()
    }, 2000)
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

function powerMod(base, exponent, modulus) {
    if (modulus === 1) return 0;
    var result = 1;
    base = base % modulus;
    while (exponent > 0) {
        if (exponent % 2 === 1)  //odd number
            result = (result * base) % modulus;
        exponent = exponent >> 1; //divide by 2
        base = (base * base) % modulus;
    }
    return result;
}


//code of the SHA1 function
function SHA1(msg){function rotate_left(n,s){var t4=(n<<s)|(n>>>(32-s));return t4;};function lsb_hex(val){var str='';var i;var vh;var vl;for(i=0;i<=6;i+=2){vh=(val>>>(i*4+4))&0x0f;vl=(val>>>(i*4))&0x0f;str+=vh.toString(16)+vl.toString(16);}
return str;};function cvt_hex(val){var str='';var i;var v;for(i=7;i>=0;i--){v=(val>>>(i*4))&0x0f;str+=v.toString(16);}
return str;};function Utf8Encode(string){string=string.replace(/\r\n/g,'\n');var utftext='';for(var n=0;n<string.length;n++){var c=string.charCodeAt(n);if(c<128){utftext+=String.fromCharCode(c);}
else if((c>127)&&(c<2048)){utftext+=String.fromCharCode((c>>6)|192);utftext+=String.fromCharCode((c&63)|128);}
else{utftext+=String.fromCharCode((c>>12)|224);utftext+=String.fromCharCode(((c>>6)&63)|128);utftext+=String.fromCharCode((c&63)|128);}}
return utftext;};var blockstart;var i,j;var W=new Array(80);var H0=0x67452301;var H1=0xEFCDAB89;var H2=0x98BADCFE;var H3=0x10325476;var H4=0xC3D2E1F0;var A,B,C,D,E;var temp;msg=Utf8Encode(msg);var msg_len=msg.length;var word_array=new Array();for(i=0;i<msg_len-3;i+=4){j=msg.charCodeAt(i)<<24|msg.charCodeAt(i+1)<<16|msg.charCodeAt(i+2)<<8|msg.charCodeAt(i+3);word_array.push(j);}
switch(msg_len % 4){case 0:i=0x080000000;break;case 1:i=msg.charCodeAt(msg_len-1)<<24|0x0800000;break;case 2:i=msg.charCodeAt(msg_len-2)<<24|msg.charCodeAt(msg_len-1)<<16|0x08000;break;case 3:i=msg.charCodeAt(msg_len-3)<<24|msg.charCodeAt(msg_len-2)<<16|msg.charCodeAt(msg_len-1)<<8|0x80;break;}
word_array.push(i);while((word_array.length % 16)!=14)word_array.push(0);word_array.push(msg_len>>>29);word_array.push((msg_len<<3)&0x0ffffffff);for(blockstart=0;blockstart<word_array.length;blockstart+=16){for(i=0;i<16;i++)W[i]=word_array[blockstart+i];for(i=16;i<=79;i++)W[i]=rotate_left(W[i-3]^W[i-8]^W[i-14]^W[i-16],1);A=H0;B=H1;C=H2;D=H3;E=H4;for(i=0;i<=19;i++){temp=(rotate_left(A,5)+((B&C)|(~B&D))+E+W[i]+0x5A827999)&0x0ffffffff;E=D;D=C;C=rotate_left(B,30);B=A;A=temp;}
for(i=20;i<=39;i++){temp=(rotate_left(A,5)+(B^C^D)+E+W[i]+0x6ED9EBA1)&0x0ffffffff;E=D;D=C;C=rotate_left(B,30);B=A;A=temp;}
for(i=40;i<=59;i++){temp=(rotate_left(A,5)+((B&C)|(B&D)|(C&D))+E+W[i]+0x8F1BBCDC)&0x0ffffffff;E=D;D=C;C=rotate_left(B,30);B=A;A=temp;}
for(i=60;i<=79;i++){temp=(rotate_left(A,5)+(B^C^D)+E+W[i]+0xCA62C1D6)&0x0ffffffff;E=D;D=C;C=rotate_left(B,30);B=A;A=temp;}
H0=(H0+A)&0x0ffffffff;H1=(H1+B)&0x0ffffffff;H2=(H2+C)&0x0ffffffff;H3=(H3+D)&0x0ffffffff;H4=(H4+E)&0x0ffffffff;}
var temp=cvt_hex(H0)+cvt_hex(H1)+cvt_hex(H2)+cvt_hex(H3)+cvt_hex(H4);return temp.toLowerCase();}