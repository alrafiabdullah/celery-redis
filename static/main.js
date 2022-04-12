document.addEventListener('DOMContentLoaded', () => {
    let ttl = document.getElementById('ttl');

    const secondInterval = setInterval(() => {
        axios.get("/cache/time")
            .then(res => {
                ttl.textContent = res.data.ttl;
                if (parseInt(ttl.textContent) < 30) {
                    ttl.style.color = 'red';
                } else {
                    ttl.style.color = 'green';
                }
            })
            .catch(err => {
                console.log(err);
            });
        try {
            if (parseInt(ttl.textContent) < 1) {
                clearInterval(secondInterval);
            }
        } catch (e) {
            clearInterval(secondInterval);
        }
    }, 1000);

});