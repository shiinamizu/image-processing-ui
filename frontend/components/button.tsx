import React from 'react';
import clsx from 'clsx';
import styles from '@/components/button.css';


type ButtonProps = React.ComponentPropsWithRef<"button"> & {
    /**
     * @default "natural"
     */
    variant?: "primary" | "secondary" | "natural";
  };
  
  const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
    (props, ref) => {
      const { variant = "natural", className, ...restProps } = props;
  
      return (
        <button
          // className={clsx(styles.button, className)}
          data-variant={variant}
          {...restProps}
          ref={ref}
        />
      );
    }
  );
  
  Button.displayName = "Button";
  
  export {Button};