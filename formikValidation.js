import { useFormik } from "formik";
import React, { useContext, useState } from "react";
import ReactjsAlert from "reactjs-alert";
import { main } from "../ContextApi";
import "./loginform.css";

export default function LogInForm() {
  const auth = useContext(main);
  // ========reactjs-alert=========
  const [alertShow, setAlertShow] = useState(false);
  const [alertType, setAlertType] = useState("");
  const [alertTitle, setAlertTitle] = useState("");
  // ===========
  const validate = (values) => {
    const errors = {};
    if (!values.name) {
      errors.name = "The name field is required";
    }
    if (!values.email) {
      errors.email = "The email field is required";
    } else if (
      !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)
    ) {
      errors.email = "Provide valid email";
    }
    if (!values.password) {
      errors.password = "The password field is required";
    } else if (values.password.length < 4 || values.password.length > 10) {
      errors.password = "Provide 4 to 10 digit password";
    }
    if (!values.confirmpassword) {
      errors.confirmpassword = "The Confirm password is required";
    } else if (values.password !== values.confirmpassword) {
      errors.confirmpassword = "Password and ConfirmPassword not match";
    }
    if (!values.dob) {
      errors.dob = "The DOB is required";
    }
    return errors;
  };
  const [values, setValues] = useState();
  const formik = useFormik({
    initialValues: {
      name: "",
      email: "",
      password: "",
      confirmpassword: "",
    },
    validate,

    onSubmit: (values) => {
      setValues(values);
      const age = getAge(values.dob);
      if (age > 15) {
        auth.setStudent(values);
        auth.isStudentLogIn();
      } else if (age < 15) {
        setAlertTitle("Your Not Elible to 10th");
        setAlertType("error");
        setAlertShow(true);
      }
    },
  });
  //   ========calculateAge========
  function getAge(dob) {
    var today = new Date();
    var birthDate = new Date(dob);
    var age = today.getFullYear() - birthDate.getFullYear();
    var month = today.getMonth() - birthDate.getMonth();
    if (month < 0 || (month === 0 && today.getMonth() < birthDate.getMonth())) {
      age--;
    }
    return age;
  }
  // =========
  const handleEnter = (e) => {
    if (e.key.toLowerCase() === "enter") {
      const form = e.target.form;
      const index = [...form].indexOf(e.target);
      form.elements[index + 1].focus();

      e.preventDefault();
    }
  };
  return (
    <div>
      <form className="log-in-form" onSubmit={formik.handleSubmit}>
        <h2>LogIn Form</h2>
        <label>Name</label>
        <input
          onKeyDown={handleEnter}
          type="text"
          name="name"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
        />
        {formik.touched.name && formik.errors.name ? (
          <div className="error-message-new">{formik.errors.name}</div>
        ) : null}
        <label>Email</label>
        <input
          onKeyDown={handleEnter}
          type="text"
          name="email"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
        />
        {formik.touched.email && formik.errors.email ? (
          <div className="error-message-new">{formik.errors.email}</div>
        ) : null}
        <label>password</label>
        <input
          onKeyDown={handleEnter}
          type="password"
          name="password"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
        />
        {formik.touched.password && formik.errors.password ? (
          <div className="error-message-new">{formik.errors.password}</div>
        ) : null}
        <label>Confirm password</label>
        <input
          onKeyDown={handleEnter}
          type="password"
          name="confirmpassword"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
        />
        {formik.touched.confirmpassword && formik.errors.confirmpassword ? (
          <div className="error-message-new">
            {formik.errors.confirmpassword}
          </div>
        ) : null}
        <label>DOB</label>
        <input
          onKeyDown={handleEnter}
          type="date"
          name="dob"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
        />
        <div className="log-in-button">
          <button type="submit">Log In</button>
        </div>
      </form>
      <ReactjsAlert
        status={alertShow}
        type={alertType}
        title={alertTitle}
        Close={() => setAlertShow(false)}
      />
    </div>
  );
}
