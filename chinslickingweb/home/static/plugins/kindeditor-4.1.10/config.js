
var editor = new Array();
var options = {
    filterMode : true,
    allowImageUpload : false,
    allowFlashUpload : false,
    allowMediaUpload : false,
    allowFileManager : false,
    items : ['fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
    'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
    'insertunorderedlist', '|', 'emoticons', 'image', 'flash', 'media','|', 'link','unlink','fullscreen'],
    width : '800px',
    height: '600px'
};
var options1 = {
    width:'800px',
    height:'600px',
    resizeType:1,
    allowPreviewEmoticons: false,
    allowImageRemote: false,
    uploadJson: '/admin/upload/kindeditor',
};

KindEditor.ready(function(K){
    editor[0] = K.create('textarea[name=content]', options1);
    editor[1] = K.create('textarea[name=en_content]', options1);
    editor[2] = K.create('textarea[name=short_content]', options1);
    editor[3] = K.create('textarea[name=long_content]', options1);
    editor[4] = K.create('textarea[name=en_short_content]', options1);
    editor[5] = K.create('textarea[name=en_long_content]', options1);
});