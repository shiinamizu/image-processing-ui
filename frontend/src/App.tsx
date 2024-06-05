import { useState } from 'react';
import './App.css';
import { Button } from '@/components/button';
import {ImageComponent} from '@/components/get-image';

// import {Hello} from '@/components/hello';
function App() {
  const [count, setCount] = useState(0)
  
  return (
    <div>
        <div>
          ここに記述

         
          
          </div>  
          <Button variant="primary">Primary Button</Button>
          <Button className="test" type="submit" variant="primary">
              登録
            </Button>
            <ImageComponent />
            {/* <Hello /> */}

    
      </div>
  )
}

export default App
