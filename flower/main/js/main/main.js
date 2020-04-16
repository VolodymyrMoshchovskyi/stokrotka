const button = document.querySelector('.c-hamburger');
const menuMobile = document.querySelector('.menu-mobile');
const xxx = document.querySelector('#xxx');

button.onclick = function () {
    this.classList.toggle('is-active');
    menuMobile.classList.toggle('left');
};

let dropMenu = document.querySelector('.drop-down-mobile');

xxx.onclick = () => {
    dropMenu.classList.toggle('is-active');

    if (dropMenu.classList.contains('is-active')) {
        dropMenu.style.height = dropMenu.scrollHeight + 'px';
    } else {
        dropMenu.style.height = '';
    }
};