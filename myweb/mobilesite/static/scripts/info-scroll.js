let startx, starty
let parentEle = null
const infoEle = document.getElementById('info-block')

//手指接触屏幕
document.addEventListener("touchstart", function(e) {
    let currentElement = event.target
    console.log('currentElement', currentElement)
    parentEle = currentElement.parentNode
    console.log('parentEle', parentEle)
    while(parentEle && parentEle.parentNode !== document.body){
        parentEle = parentEle.parentNode
    }
    startx = e.touches[0].pageX
    starty = e.touches[0].pageY
}, false)

//手指离开屏幕
document.addEventListener("touchend", function(e) {
    let endx, endy
    endx = e.changedTouches[0].pageX
    endy = e.changedTouches[0].pageY
    let direction = getDirection(startx, starty, endx, endy)
    if(parentEle === infoEle)
    switch (direction) {
        case 1:
            infoEle.classList.add('active')  
            // document.body.style.overflow = 'scroll'
            break;
        case 2:
            infoEle.classList.remove('active')
            // document.body.style.overflow = 'hidden'
            break;
        default:
    }
}, false)

//获得角度
function getAngle(angx, angy) {
    return Math.atan2(angy, angx) * 180 / Math.PI
}

//根据起点终点返回方向 1向上 2向下 3向左 4向右 0未滑动
function getDirection(startx, starty, endx, endy) {
    let angx = endx - startx
    let angy = endy - starty
    let result = 0

    //如果滑动距离太短
    if (Math.abs(angx) < 2 && Math.abs(angy) < 2) {
        return result
    }

    let angle = getAngle(angx, angy)
    if (angle >= -135 && angle <= -45) {
        result = 1
    } else if (angle > 45 && angle < 135) {
        result = 2
    } else if ((angle >= 135 && angle <= 180) || (angle >= -180 && angle < -135)) {
        result = 3
    } else if (angle >= -45 && angle <= 45) {
        result = 4
    }

    return result
}