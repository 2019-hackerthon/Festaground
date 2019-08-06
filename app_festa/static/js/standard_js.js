window.onload = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.menuDisplay();
}
window.onresize = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.menuDisplay();
}

function menuDisplay(){
    var nowMenuView = document.getElementById('now_menu_wrapper');
    nowMenuView.style.display = 'block';
}