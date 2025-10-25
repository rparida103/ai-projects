Here’s a simple implementation of a calculator app based on the design plan you provided. This implementation will focus on the core functionality, including the calculator engine, user interface, and basic error handling. For simplicity, I will use React for the web version.

### Directory Structure

```
/calculator-app
├── /src
│   ├── /components
│   │   ├── Calculator.js
│   │   ├── Button.js
│   │   ├── Display.js
│   ├── /utils
│   │   ├── calculatorEngine.js
│   ├── /styles
│   │   ├── App.css
│   ├── App.js
│   ├── index.js
├── /tests
│   ├── calculatorEngine.test.js
│   ├── App.test.js
├── package.json
├── README.md
```

### 1. `calculatorEngine.js` (Calculator Logic)

```javascript
// src/utils/calculatorEngine.js

export const calculate = (input) => {
    try {
        // Basic validation
        if (!input) return "0";
        // Evaluate the expression
        const result = eval(input); // Note: eval can be dangerous, use with caution
        if (result === Infinity) throw new Error("Division by zero");
        return result.toString();
    } catch (error) {
        return "Error";
    }
};
```

### 2. `Button.js` (Button Component)

```javascript
// src/components/Button.js

import React from 'react';

const Button = ({ label, onClick }) => {
    return (
        <button onClick={() => onClick(label)} className="button">
            {label}
        </button>
    );
};

export default Button;
```

### 3. `Display.js` (Display Component)

```javascript
// src/components/Display.js

import React from 'react';

const Display = ({ value }) => {
    return (
        <div className="display">
            {value}
        </div>
    );
};

export default Display;
```

### 4. `Calculator.js` (Main Calculator Component)

```javascript
// src/components/Calculator.js

import React, { useState } from 'react';
import Button from './Button';
import Display from './Display';
import { calculate } from '../utils/calculatorEngine';
import './App.css';

const Calculator = () => {
    const [input, setInput] = useState('');
    const [result, setResult] = useState('0');

    const handleButtonClick = (label) => {
        if (label === 'C') {
            setInput('');
            setResult('0');
        } else if (label === '=') {
            const computedResult = calculate(input);
            setResult(computedResult);
            setInput('');
        } else {
            setInput(prev => prev + label);
        }
    };

    const buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ];

    return (
        <div className="calculator">
            <Display value={input || result} />
            <div className="button-grid">
                {buttons.map((label) => (
                    <Button key={label} label={label} onClick={handleButtonClick} />
                ))}
            </div>
        </div>
    );
};

export default Calculator;
```

### 5. `App.js` (Main Application)

```javascript
// src/App.js

import React from 'react';
import Calculator from './components/Calculator';
import './styles/App.css';

const App = () => {
    return (
        <div className="app">
            <h1>Simple Calculator</h1>
            <Calculator />
        </div>
    );
};

export default App;
```

### 6. `index.js` (Entry Point)

```javascript
// src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles/App.css';

ReactDOM.render(<App />, document.getElementById('root'));
```

### 7. `App.css` (Styling)

```css
/* src/styles/App.css */

.app {
    text-align: center;
    margin: 20px;
}

.calculator {
    display: inline-block;
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 10px;
}

.display {
    font-size: 2em;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
}

.button-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}

.button {
    padding: 20px;
    font-size: 1.5em;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
}

.button:hover {
    background-color: #0056b3;
}
```

### 8. Testing

You can create unit tests for the calculator engine and integration tests for the main application using a testing library like Jest.

#### Example of `calculatorEngine.test.js`

```javascript
// tests/calculatorEngine.test.js

import { calculate } from '../src/utils/calculatorEngine';

describe('Calculator Engine', () => {
    test('adds two numbers', () => {
        expect(calculate('2+2')).toBe('4');
    });

    test('handles division by zero', () => {
        expect(calculate('2/0')).toBe('Error');
    });

    test('returns error for invalid input', () => {
        expect(calculate('2+')).toBe('Error');
    });
});
```

### 9. Package.json

You will need to initialize your project with `npm init` and install React and ReactDOM:

```bash
npm install react react-dom
```

### 10. Running the App

To run the application, you can use Create React App or set up your own Webpack configuration. If using Create React App, simply run:

```bash
npm start
```

### Summary

This implementation provides a basic calculator with a responsive UI, input handling, and error management. You can enhance it further by adding more features, improving the UI, and implementing more robust error handling.