package com.example.nicholas.sturdyrobot;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.example.nicholas.sturdyrobot.dummy.DummyContent;

public class MainActivity extends AppCompatActivity
        implements MenuFragment.OnListFragmentInteractionListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if(findViewById(R.id.fragment_box)!= null){
            if(savedInstanceState != null){
                return;
            }
        }

        MenuFragment menuFragment = new MenuFragment();
        getSupportFragmentManager()
                .beginTransaction()
                .add(menuFragment, "MenuFragment")
                .commit();
    }

    public void onListFragmentInteraction(DummyContent.DummyItem item){

    }
}
