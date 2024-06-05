import React, { useState, useEffect} from 'react';
import axios from 'axios';

const Hello = ()=>{
    useEffect(() => {
        axios.get('/')
        .then(res => {
            setPosts(res.data)
        })
    }, [])

    return <div> {res.data} </div>

}

export {Hello};