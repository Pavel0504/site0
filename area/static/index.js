class Page {
    constructor() {
        this.finder = new PageFinder();
        this.element = new PageElement();
    }
    
    addInit(func) {
        window.addEventListener('load', func);
    }
    
    element() {
        return this.element;
    }
    
    get() {
        return this.finder;
    }
}

class PageElement {
    create(elementName, attributeList, classList) {
        const element = document.createElement(elementName);

        for (let a in attributeList) {
            element.setAttribute(a, attributeList[a]);
        }
        
        for (let i in classList) {
            element.classList.add(classList[i]);
        }
        
        return element;
    }
    
    isEnabled(element, func) {
        if (func()) {
            element.removeAttribute('disabled');
        } else {
            element.setAttribute('disabled', 'disabled');            
        }
    }
    
    bindAll(selectorOrElementList, event, func) {
        const elementList = typeof selectorOrElementList === 'string'
            ? document.querySelectorAll(selectorOrElementList)
            : selectorOrElementList;
            
        for (let el of elementList) {
            this.bind(el, event, func);
        }
    }
    
    bind(selectorOrElementList, event, func) {
        const element = typeof selectorOrElementList === 'string'
            ? document.querySelector(selectorOrElementList)
            : selectorOrElementList;
        element.addEventListener(event, func);
    }
}

class PageFinder {
    all(sel) {
        return document.querySelectorAll(sel);
    }
    
    one(sel) {
        const ret = document.querySelector(sel);
        return ret;
    }
    
    byClass(className) {
        return document.getElementsByClassName(className);
    }
    
    byId(id) {
        return document.getElementById(id);
    }
}
