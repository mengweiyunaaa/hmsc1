;
var common_ops = {
    init:function () {
        console.log('init的common.js')
        this.eventBind()
    },
    eventBind:function () {
        console.log('hahahah')
    },
    buildUrl:function (path,params) {
        var url = "" + path;
        console.log('--------');
        console.log('url'+ url);
        console.log(1);
        return url
    }
};
$(document).ready(function () {
    common_ops.init();
    common_ops.buildUrl();

});