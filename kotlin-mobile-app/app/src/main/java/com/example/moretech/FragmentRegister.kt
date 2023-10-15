package com.example.moretech

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.Toast
import androidx.lifecycle.ViewModelProvider
import com.example.moretech.viewmodels.AuthViewModel
import com.google.android.material.textfield.TextInputEditText

// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

/**
 * A simple [Fragment] subclass.
 * Use the [FragmentRegister.newInstance] factory method to
 * create an instance of this fragment.
 */
class FragmentRegister : Fragment() {

    lateinit var tfRegisterUser: TextInputEditText
    lateinit var tfRegisterPassword: TextInputEditText
    lateinit var btnSignUp: Button
    private lateinit var authViewModel: AuthViewModel



    private var param1: String? = null
    private var param2: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        authViewModel = ViewModelProvider(this).get(AuthViewModel::class.java)

        arguments?.let {
            param1 = it.getString(ARG_PARAM1)
            param2 = it.getString(ARG_PARAM2)
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        val view = inflater.inflate(R.layout.fragment_register, container, false)

        tfRegisterUser = view.findViewById(R.id.tf_registerUser)
        tfRegisterPassword = view.findViewById(R.id.tf_registerPassword)
        btnSignUp = view.findViewById(R.id.btn_signUp)

        authViewModel.idData.observe(viewLifecycleOwner) { id ->
            Toast.makeText(context, "Success, $id! Proceed to Login", Toast.LENGTH_SHORT).show()
        }

        authViewModel.error.observe(viewLifecycleOwner) { errorMessage ->
            if (!errorMessage.isNullOrEmpty()) {
                Toast.makeText(context, errorMessage, Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(context, "Success! Proceed to Login", Toast.LENGTH_SHORT).show()
            }
        }

        btnSignUp.setOnClickListener {
            val username = tfRegisterUser.text.toString()
            val password = tfRegisterPassword.text.toString()
            authViewModel.registerId(username, password)
        }

        return view
    }


    companion object {
        @JvmStatic
        fun newInstance(param1: String, param2: String) =
            FragmentRegister().apply {
                arguments = Bundle().apply {
                    putString(ARG_PARAM1, param1)
                    putString(ARG_PARAM2, param2)
                }
            }
    }
}