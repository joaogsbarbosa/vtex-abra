/* Form 1 */
form1 = document.getElementById('form1')
dbHost = document.getElementById('host')
dbUsername = document.getElementById('username')
dbPassword = document.getElementById('password')
dbName = document.getElementById('dbname')
btnForm1 = document.getElementById('btn-form1')
dbStatus = document.getElementById('db-status')

/* Form 2 */
form2 = document.getElementById('form2')
url = document.getElementById('url')
lblHeaders = document.getElementById('lbl-headers')
headers = document.getElementById('headers')
btnForm2Add = document.getElementById('btn-form2-add')
btnForm2Rem = document.getElementById('btn-form2-rem')
btnForm2Con = document.getElementById('btn-form2-con')
btnForm2 = document.getElementById('btn-form2')

/* Form 3 */
form3 = document.getElementById('form3')
respModel = document.getElementById('response-model')
btnForm3Skp = document.getElementById('btn-form3-skp')
respModelKeys = document.getElementsByClassName('key')

/* Form 4 */
form4 = document.getElementById('form4')
table = document.getElementById('table')
btnForm4 = document.getElementById('btn-form4')


btnForm1.onclick = function () {
    axios.post('/api/1', data = {
        host: dbHost.value,
        username: dbUsername.value,
        password: dbPassword.value,
        dbname: dbName.value
    }).then(function (response) {
        dbStatus.textContent = 'Sucesso!'
        dbStatus.className = 'alert alert-success'
        form1.style.display = 'none'
        form2.style.display = 'block'
        disableChild(form1)
    }).catch(function (error) {
        dbStatus.textContent = 'Erro!'
        dbStatus.className = 'alert alert-danger'
    })
}

btnForm2Add.onclick = function () {
    span = document.createElement('span')
    input1 = document.createElement('input')
    input1.classList.add('col-5')
    input1.setAttribute('name', 'key')
    separator = document.createElement('span')
    separator.textContent = ':'
    input2 = document.createElement('input')
    input2.classList.add('col-6')
    input2.setAttribute('name', 'value')
    span.appendChild(input1)
    span.appendChild(separator)
    span.appendChild(input2)
    headers.append(span)
}

btnForm2Rem.onclick = function () {
    headers.removeChild(headers.lastElementChild)
}

btnForm2Con.onclick = function () {
    keys = document.getElementsByName('key')
    values = document.getElementsByName('value')
    headersDict = {}
    for (i = 0; i < keys.length; i++) {
        headersDict[keys[i].value] = values[i].value
    }
    axios.get(url.value.replace('{}', '1'), headersDict
    ).then(function (response) {
        form2.style.display = 'none'
        form3.style.display = 'block'
        disableChild(form2)
        form3Load(response)
    }).catch(function (error) {
        window.alert(error)
    })
}

function form3Load(response) {
    if (Array.isArray(response.data))
        respCutted = response.data[0]
    else
        respCutted = response.data

    for (i = 0; i < Object.entries(respCutted).length; i++) {
        for (o = 0; o < Object.entries(respCutted)[i].length; o++) {
            if (typeof Object.entries(respCutted)[i][o] == "object") {
                var hasArray = true
                break
            }
        }
    }
    path = ""
    if (typeof hasArray !== 'undefined') {
        //respModel.textContent = JSON.stringify(respCutted, undefined, 2)
        respModel.innerHTML = syntaxHighlight(respCutted)

        document.querySelectorAll('.key').forEach(e => {
            if (e.nextSibling.textContent.includes('{')) {
                e.classList.add('objKey')

                e.addEventListener('click', event => {
                    path=e.textContent.replace('\"', '').replace('\":', '')
                    chaveFechando=0

                    while (e.className.includes("key") || e.className.includes("string") || e.className.includes("number") || e.className.includes("boolean") || e.className.includes("null")) {
                        if(e.previousSibling.textContent.includes('}')) {
                            e.previousSibling.textContent.split('').forEach(letter => {
                                if (letter == '}')
                                    chaveFechando+=1
                            })
                        }
                        if(e.previousSibling.textContent.includes('{')) {
                            e.previousSibling.textContent.split('').forEach(letter => {
                                if (letter == '{')
                                    chaveFechando-=1
                            })
                            if (chaveFechando < 0) {
                                if (e.previousElementSibling) {
                                    path = e.previousElementSibling.textContent.replace('\"', '').replace('\":', '') + '/' + path
                                    chaveFechando = 0
                                }
                                else
                                    break
                            }
                        }
                        if (e.previousElementSibling)
                            e = e.previousElementSibling
                        else
                            break
                    }

                    form3.style.display = 'none'
                    form4.style.display = 'block'
                    disableChild(form3)
                })
            }
        })
    }
    else {
        form3.style.display = 'none'
        form4.style.display = 'block'
        disableChild(form3)
    }
}

btnForm3Skp.onclick = function () {
    form3.style.display = 'none'
    form4.style.display = 'block'
    disableChild(form3)
}

btnForm4.onclick = function () {
    axios.post('/api/2', data = {
        'url': url.value,
        'headers': headersDict,
        'path': path,
        'table_name': table.value
    }).then(response => {
        window.alert('Sucesso!', response.data)
    }).catch(error => {
        window.alert('Erro!', error.data)
    })
}

function disableChild(element) {
    var nodes = element.getElementsByTagName('*');
    for (var i = 0; i < nodes.length; i++) {
        nodes[i].disabled = true;
    }
}

function syntaxHighlight(json) {
    if (typeof json != 'string') {
        json = JSON.stringify(json, undefined, 2);
    }
    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}