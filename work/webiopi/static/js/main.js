webiopi()
 
function python() {
    webiopi().callMacro("run_script", 0, callbackGetValue);
}
 
function callbackGetValue(macro, args, data) {
    console.log(macro);
    console.log(args);
    console.log(data);
}