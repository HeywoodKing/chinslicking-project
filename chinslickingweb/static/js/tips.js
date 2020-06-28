
(function ($) {

    //随机显示气泡提示语
    var divTips = [
        'ArrowLeft',
        'ArrowRight',
        'ArrowDownRight',
        'ArrowDownLeft'
    ];
    var tips = [
        '听说浇水888次，可以结一个水果哦',
        '水果可以兑换成秦食皇礼物呢',
        '口渴了……没人给我浇水么？',
        '亲朋好友如相问，种棵真树传真情',
        '给我浇水我就能长大哦',
        '我渴了，快来给我浇水吧！',
        '结果实抢优惠券哦',
        '天大地大，我要快快长大！'
    ];

    /**
     * 气泡提示
     * @return {}
     */
    function run() {
        var i = random(0, divTips.length);
        var j = random(0, tips.length);
        var fadeOutTime = 3500, fadeInTime = 8000;
        $('#' + divTips[i]).children('.box-dialog').children('.box-body').html(tips[j]);
        $('#' + divTips[i]).removeClass('hidden fadeOut').addClass('fadeIn');
        var timerTipsFadeOut = setTimeout(function () {
            $('#' + divTips[i]).addClass('fadeOut');
            timerTipsFadeOut = null;
        }, fadeOutTime);

        var timerTipsFadeIn = setInterval(function () {
            i = random(0, divTips.length);
            j = random(0, tips.length);
            $('#' + divTips[i]).children('.box-dialog').children('.box-body').html(tips[j]);
            $('#' + divTips[i]).removeClass('hidden fadeOut').addClass('fadeIn');

            if (!timerTipsFadeOut) {
                timerTipsFadeOut = setTimeout(function () {
                    $('#' + divTips[i]).addClass('fadeOut');
                    timerTipsFadeOut = null;
                }, fadeOutTime);
            }
        }, fadeInTime + fadeOutTime);
    }

    /**
     * 产生随机整数，包含下限值，但不包括上限值
     * @param {Number} lower 下限
     * @param {Number} upper 上限
     * @return {Number} 返回在下限到上限之间的一个随机整数
     */
    function random(lower, upper){
        return Math.floor(Math.random() * (upper - lower)) + lower;
    }

    /**
     * 产生随机整数，包含下限值，包括上限值
     * @param {Number} lower 下限
     * @param {Number} upper 上限
     * @return {Number} 返回在下限到上限之间的一个随机整数
     */
    function randomUpper(lower, upper) {
        return Math.floor(Math.random() * (upper - lower+1)) + lower;
    }

    /**
     * 产生一个随机的rgb颜色
     * @return {String}  返回颜色rgb值字符串内容，如：rgb(201, 57, 96)
     */
    function randomColor() {
        // 随机生成 rgb 值，每个颜色值在 0 - 255 之间
        var r = random(0, 256),
            g = random(0, 256),
            b = random(0, 256);
        // 连接字符串的结果
        var result = "rgb("+ r +","+ g +","+ b +")";
        // 返回结果
        return result;
    }

    //运行气泡提示
    run();

})(jQuery);
