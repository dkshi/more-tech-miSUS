package com.example.moretech

import android.content.Intent
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.lifecycleScope
import com.example.moretech.datastore.DataStoreManagerSingleton
import com.example.moretech.viewmodels.AuthViewModel
import com.google.android.material.textfield.TextInputEditText
import kotlinx.coroutines.launch

// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

/**
 * A simple [Fragment] subclass.
 * Use the [FragmentLogin.newInstance] factory method to
 * create an instance of this fragment.
 */
class FragmentLogin : Fragment() {

    lateinit var tfLoginUser: TextInputEditText
    lateinit var tfLoginPassword: TextInputEditText
    lateinit var btnSignIn: Button
    private lateinit var authViewModel: AuthViewModel
    lateinit var token: String


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
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_login, container, false)

        authViewModel.checkToken()

        authViewModel.checkToken.observe(viewLifecycleOwner){check ->
            if(check.ok){
                val intent = Intent(context, MapActivity::class.java)
                    //startActivity(intent)
            }
        }

        tfLoginUser = view.findViewById(R.id.tf_loginUser)
        tfLoginPassword = view.findViewById(R.id.tf_loginPassword)
        btnSignIn = view.findViewById(R.id.btn_signIn)

        authViewModel.tokenData.observe(viewLifecycleOwner) { newtoken ->
            lifecycleScope.launch {
                DataStoreManagerSingleton.dataStore.storeString(newtoken.toString())
                DataStoreManagerSingleton.token = newtoken.toString()
            }
        }

        authViewModel.error.observe(viewLifecycleOwner) { errorMessage ->
            if (!errorMessage.isNullOrEmpty()) {
                Toast.makeText(view.context, errorMessage, Toast.LENGTH_SHORT).show()
            }


        }
        btnSignIn.setOnClickListener {
            val username = tfLoginUser.text.toString()
            val password = tfLoginPassword.text.toString()
            authViewModel.recieveToken(username, password)
            authViewModel.checkToken()
            val intent = Intent(view.context, MapActivity::class.java)
            startActivity(intent)

        }
        return view
    }

    companion object {
        @JvmStatic
        fun newInstance(param1: String, param2: String) =
            FragmentLogin().apply {
                arguments = Bundle().apply {
                    putString(ARG_PARAM1, param1)
                    putString(ARG_PARAM2, param2)
                }
            }
    }
}