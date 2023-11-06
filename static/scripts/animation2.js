let sections = document.querySelectorAll('section');

window.onscroll = () => {
    sections.forEach(home => {
        let top = window.scrollY;
        let offset = home.offsetTop;
        let height = home.offsetHeight;

        if (top >= offset && top < offset + height){
            home.classList.add('show-animate');
        }else{
            home.classList.remove('show-animate');
        }
    })
}