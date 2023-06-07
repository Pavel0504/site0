//alert("hello");
function init(){
    const filial_el = document.getElementById("id_filial");
    filial_el.onchange = filialSelect;
    reset_company_el();
    reset_grp_el();
    reset_plot_el();
    reset_lic_el();
    bindAreaFormSubmit();
}

function filialSelect(){
    const url = "/area/" + this.value + "/filial_data";
    const company_el = reset_company_el();
    const grp_el = reset_grp_el();
    if (!this.value){return}
    axios.get(url).then(function (response){
        for (let i in response.data.company){
            company_el.innerHTML += '<option value="'+i+'">'+response.data.company[i]+'</option>'
        }
        for (let i in response.data.grp){
            grp_el.innerHTML += '<option value="'+i+'">'+response.data.grp[i]+'</option>'
        }
        grp_el.onchange = grpSelect
    }).catch(function(error){
        alert("Ошибка запроса: "+error)
    })

}

function grpSelect(){
    const url = "/area/" + this.value + "/grp_data";
    const plot_el = reset_plot_el();
    if (!this.value){return}
    axios.get(url).then(function (response){
        for (let i in response.data){
            plot_el.innerHTML += '<option value="'+i+'">'+response.data[i]+'</option>'
        }
    plot_el.onchange = plotSelect;
    }).catch(function(error){
        alert("Ошибка запроса: "+error)
    })
}

function plotSelect(){
    const url = "/area/" + this.value + "/plot_data";
    const lic_el = reset_lic_el();
    if (!this.value){return}
    axios.get(url).then(function (response){
        if (response.data){
            lic_el.innerHTML += '<option value="'+response.data.id+'">'+response.data.gos_num+" | "+response.data.name+'</option>'
        }
    }).catch(function(error){
        alert("Ошибка запроса: "+error)
    })
}

function reset_company_el(){
    const company_el = document.getElementById("id_company");
    company_el.innerHTML = '<option value="">---------</option>';
    return company_el
}

function reset_grp_el(){
    const grp_el = document.getElementById("id_grp");
    grp_el.innerHTML = '<option value="">---------</option>';
    return grp_el
}

function reset_plot_el(){
    const plot_el = document.getElementById("id_plot");
    plot_el.innerHTML = '<option value="">---------</option>';
    return plot_el
}

function reset_lic_el(){
    const lic_el = document.getElementById("id_lic");
    lic_el.innerHTML = '<option value="">---------</option>';
    return lic_el
}

window.addEventListener("load", init)

function bindAreaFormSubmit(){
    document.getElementById("area-form").onsubmit = function(e){
        e.preventDefault();
        document.getElementById("area-list").innerHTML = "...";
        const formData = this.elements;
        const data = {};
        for (let i of formData){
            data[i.name] = i.value;
        }

        data['fact'] = this.elements['fact'].checked ? 1 : 0;
        console.log(data)
        alert("Строка добавлена")
        // alert(data.csrfmiddlewaretoken);
        this.work_type.value = "";
        this.fact.checked = false;
        this.value.value = "";
        axios({
            method: 'post',
            url: '/area/add',
            data: data,
            headers: {
                'X-CSRFToken': data.csrfmiddlewaretoken,
                'X-Requested-With': 'XMLHttpRequest'
            }
        }).then(function (response){
            document.getElementById("area-list").innerHTML = response.data;
            document.getElementById('area-list').scrollIntoView();
        }).catch(function(error){

            alert("Ошибка запроса: "+error)
        })
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');